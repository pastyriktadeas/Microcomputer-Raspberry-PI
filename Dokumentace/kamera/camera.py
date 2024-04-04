from flask import Flask, render_template, Response
import datetime

video = cv2.VideoCapture(0)
app = Flask('__name__')
fgbg = cv2.createBackgroundSubtractorKNN(history=200, dist2Threshold=1000, detectShadows=False)

detected_motion_log = []

def video_stream():
    while True:
        ret, frame = video.read()
        if not ret:
            break
        else:
            fgmask = fgbg.apply(frame)
            frame = cv2.bitwise_and(frame, frame, mask=fgmask)

            # Detekce pohybu
            motion_detected = detect_motion(fgmask)

            # Přidáme informace o detekci pohybu do logu
            if motion_detected:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                detected_motion_log.append({"timestamp": timestamp, "text": "Detekce pohybu"})

            # Přidáme aktuální čas a datum na snímek
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cv2.putText(frame, f"Aktualni cas a datum: {current_datetime}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            ret, buffer = cv2.imencode('.jpeg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def detect_motion(fgmask):
    return cv2.countNonZero(fgmask) > 0

def clean_video_stream():
    while True:
        ret, frame = video.read()
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode('.jpeg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/camera')
def camera():
    return render_template('camera.html')@app.route('/motion_status')
def motion_status():
    return render_template('motion_status.html', detected_motion_log=detected_motion_log)

@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/small_video_feed')
def small_video_feed():
    return Response(clean_video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)