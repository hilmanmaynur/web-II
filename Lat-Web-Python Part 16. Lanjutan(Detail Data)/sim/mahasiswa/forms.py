from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sim.models import Tmahasiswa
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class mahasiswa_F(FlaskForm):
    npm=StringField('NPM', validators=[DataRequired(), Length(min=10, max=15)])
    nama=StringField('Nama', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired(), Email()])
    kelas=StringField('Kelas', validators=[DataRequired(), Length(min=5, max=15)])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    konf_pass=PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    alamat=TextAreaField('Alamat')
    submit=SubmitField('Tambah')

    #cek npm
    def validate_npm(self, npm):   
        ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
        if ceknpm:
            raise ValidationError("NPM Sudah Terdaftar, Gunakan NPM yang lain")
    
    #cek email
    def validate_email(self, email):
        cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError("Email Sudah Terdaftar, Gunakan Email yang lain")

class loginmahasiswa_F(FlaskForm):
    npm=StringField('NPM', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit=SubmitField('Login')

class editmahasiswa_F(FlaskForm):
    npm=StringField('NPM', validators=[DataRequired(), Length(min=10, max=15)])
    nama=StringField('Nama', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired(), Email()])
    kelas=StringField('Kelas', validators=[DataRequired(), Length(min=5, max=15)])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    konf_pass=PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    alamat=TextAreaField('Alamat')
    foto=FileField('Ubah Foto Profil', validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Ubah Data')

    #cek npm
    def validate_npm(self, npm):
        if npm.data != current_user.npm:
            ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
            if ceknpm:
                raise ValidationError("NPM Sudah Terdaftar, Gunakan NPM yang lain")
    
    #cek email
    def validate_email(self, email):
        if email.data != current_user.email:
            cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
            if cekemail:
                raise ValidationError("Email Sudah Terdaftar, Gunakan Email yang lain")

class pengaduan_F(FlaskForm):
    subjek=StringField('Subjek', validators=[DataRequired()])
    kategori=SelectField(u'Kategori Pengaduan', choices=[('Administrasi', 'Pelayanan Administrasi'), ('fasilitas', 'fasilitas'), ('Dosen', 'Dosen')], validators=[DataRequired()])
    detail_pengaduan=TextAreaField('Pengaduan', validators=[DataRequired()])
    submit=SubmitField('Kirim')

class editpengaduan_F(FlaskForm):
    subjek=StringField('Subjek', validators=[DataRequired()])
    kategori=SelectField(u'Kategori Pengaduan', choices=[('Surat', 'Pelayanan Administrasi'), ('fasilitas', 'fasilitas'), ('Dosen', 'Dosen')], validators=[DataRequired()])
    detail_pengaduan=TextAreaField('Pengaduan', validators=[DataRequired()])
    submit=SubmitField('Ubah')

class pendataan_F(FlaskForm):
    kategori_surat=SelectField(u'Jenis Surat', choices=[('Surat', 'Surat Undangan'), ('Surat Peminjaman', 'Surat Peminjaman'), ('Surat Lamaran', 'Surat Lamaran')], validators=[DataRequired()])
    surat=SelectField(u'Kategori Surat', choices=[('Surat Masuk', 'Surat Masuk'), ('Surat Keluar', 'Surat Keluar')], validators=[DataRequired()])
    detail_surat=TextAreaField('Detail Surat', validators=[DataRequired()])
    submit=SubmitField('Kirim')

class editpendataan_F(FlaskForm):
    kategori_surat=SelectField(u'Jenis Surat', choices=[('Surat', 'Surat Undangan'), ('Surat Peminjaman', 'Surat Peminjaman'), ('Surat Lamaran', 'Surat Lamaran')], validators=[DataRequired()])
    surat=SelectField(u'Kategori Surat', choices=[('Surat Masuk', 'Surat Masuk'), ('Surat Keluar', 'Surat Keluar')], validators=[DataRequired()])
    detail_surat=TextAreaField('Detail Surat', validators=[DataRequired()])
    submit=SubmitField('Ubah')