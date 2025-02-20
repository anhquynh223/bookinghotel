# Generated by Django 5.1 on 2024-11-06 17:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='khachsan',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='phong',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phong',
            name='trang_thai',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hoso',
            name='cccd',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='hoso',
            name='dia_chi',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hoso',
            name='dien_thoai',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='hoso',
            name='gioi_tinh',
            field=models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='hoso',
            name='ngay_sinh',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phong',
            name='gia',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='phong',
            name='hinh_anh1',
            field=models.ImageField(upload_to='room_images/'),
        ),
        migrations.AlterField(
            model_name='phong',
            name='hinh_anh2',
            field=models.ImageField(upload_to='room_images/'),
        ),
        migrations.AlterField(
            model_name='phong',
            name='hinh_anh3',
            field=models.ImageField(upload_to='room_images/'),
        ),
        migrations.AlterField(
            model_name='phong',
            name='khach_san',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phongs', to='booking.khachsan'),
        ),
        migrations.CreateModel(
            name='DatPhong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay_nhan', models.DateField()),
                ('ngay_tra', models.DateField()),
                ('phuong_thuc', models.CharField(choices=[('Thanh toán tại quầy', 'Thanh toán tại quầy'), ('Thanh toán chuyển khoản', 'Thanh toán chuyển khoản')], default='Thanh toán tại quầy', max_length=50)),
                ('so_tai_khoan', models.CharField(blank=True, max_length=20, null=True)),
                ('chu_the', models.CharField(blank=True, max_length=70, null=True)),
                ('trang_thai', models.CharField(choices=[('Đã hủy', 'Đã hủy'), ('Đã nhận', 'Đã nhận'), ('Hoàn thành', 'Hoàn thành')], default='Đã nhận', max_length=30)),
                ('tong_tien', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('khach_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phongdats', to=settings.AUTH_USER_MODEL)),
                ('phong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datphongs', to='booking.phong')),
            ],
        ),
        migrations.CreateModel(
            name='KhuyenMai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_km', models.CharField(max_length=20)),
                ('kieu', models.CharField(choices=[('Phần trăm', 'Phần trăm'), ('Số tiền', 'Số tiền')], max_length=20)),
                ('giam_gia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ngay_bat_dau', models.DateField()),
                ('ngay_ket_thuc', models.DateTimeField()),
                ('phong', models.ManyToManyField(blank=True, to='booking.phong')),
            ],
        ),
        migrations.CreateModel(
            name='YeuThich',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nguoi_dung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yeuthichs', to=settings.AUTH_USER_MODEL)),
                ('phong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yeuthichs', to='booking.phong')),
            ],
            options={
                'unique_together': {('nguoi_dung', 'phong')},
            },
        ),
        migrations.DeleteModel(
            name='DanhGia',
        ),
    ]
