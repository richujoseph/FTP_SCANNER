from flask import Flask, render_template, request
import ftplib
import socket

app = Flask(__name__)

def check_anonymous_ftp(ip, port=21):
    """Check if anonymous FTP login is allowed for a given IP."""
    try:
        ftp = ftplib.FTP()
        ftp.connect(ip, port, timeout=5)
        ftp.login('anonymous', 'anonymous')
        ftp.quit()
        return True
    except ftplib.error_perm:
        return False
    except (socket.timeout, ConnectionRefusedError, ftplib.error_temp):
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    if request.method == 'POST':
        target = request.form.get('target')
        if target:
            try:
                ip = socket.gethostbyname(target)
                status = check_anonymous_ftp(ip)
                results[target] = 'Anonymous FTP Allowed' if status else 'Access Denied' if status is False else 'No FTP Service'
            except socket.gaierror:
                results[target] = 'Invalid Hostname'
    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
