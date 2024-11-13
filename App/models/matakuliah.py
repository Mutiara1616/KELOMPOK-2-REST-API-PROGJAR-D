from App.extensions import db

class MataKuliahModel(db.Model):
    __tablename__ = 'matakuliah'
    
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kode = db.Column(db.String(10), unique=True, nullable=False)
    sks = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"MataKuliah(nama={self.nama}, kode={self.kode}, sks={self.sks})"