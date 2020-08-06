from transactions_downloader import db
import datetime


class ImportLog(db.Model):
    __tablename__ = 'IMPORT_LOG'

    file_id = db.Column(db.Integer, primary_key=True)
    file_nm = db.Column(db.String(40), nullable=True, unique=True)
    operation_dt = db.Column(db.Date, nullable=False)
    download_dtm = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    download_msg = db.Column(db.String(100), nullable=True)
    import_flg = db.Column(db.String(1), nullable=True, default=' ')
    etl_flg = db.Column(db.String(1), nullable=True, default=' ')

    def __repr__(self):
        return f"ImportLog('{self.file_nm}', '{self.operation_dt}', '{self.download_dtm}', '{self.download_msg}', '{self.import_flg}', '{self.etl_flg}')"
