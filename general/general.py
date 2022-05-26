from config import *

BLP_general = Blueprint('BLP_general', __name__,
                        template_folder='templates',
                        static_folder='static')


@BLP_general.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('BLP_general.download_file', name=filename))
    return render_template('general/index.html')


@BLP_general.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], name)
