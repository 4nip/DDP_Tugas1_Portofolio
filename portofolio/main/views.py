from django.shortcuts import render

def home(request):
    context = {
        'name' : 'LUTFI HANIF',
        'title' : 'student',
        'bio' : 'Saya adalah seorang mahasiswa yang pinter dan ganteng'
    }
    return render(request,'main/home.html', context)

def about(request):
    context = {
        'education' : [
            {
                'degree' : 'PAUD',
                'institution' : 'Paud Flamboyan',
                'majority' : 'Taman Kanak-kanak',
                'year' : '2013-2018'
            },
            {
                'degree' : 'SD',
                'institution' : 'SDN Curug',
                'year' : '2012-2013'
            },
            {
                'degree' : 'SMP',
                'institution' : 'SMP Generasi Madani',
                'year' : '2019-2021',
                'gpa' : '87.5'
            },
            {
                'degree' : 'SMK',
                'institution' : 'SMKN 1 Cibinong',
                'majority' : 'Multimedia',
                'year' : '2021-2024',
                'gpa' : '86.5'
            },
            {
                'degree' : 'Universitas',
                'institution' : 'STT Terpadu Nurul Fikri',
                'majority' : 'Teknik Informatika',
                'year' : '2025-to date',
                'gpa' : '-'
            }
        ],

        'experience' : [
            {
                'company': 'PT. Indocement TBK ',
                'role': 'Video Editor Intern',
                'periode': 'Jan 2023 - April 2023',
                'description': 'Mengedit video pembelajar karyawan indocement.'
            },
            {
                'company': 'B One Corporation',
                'role': 'Desain Grafis Intern',
                'periode': 'Jul 2023 - Sep 2023',
                'description': 'Membantu pembuatan aset visual untuk konten media sosial dan branding klien.'
            },
            {
                'company': 'Kp. Cipayung RT 03/05',
                'role': 'Ketua Panitia 17 Agustus',
                'periode': 'Agus 2022',
                'description': 'Menjadi Ketua acara HUT RI Ke-75 di Kp. Cipayung'
            },
            {
                'role': 'Humas',
                'company': 'Badminton SMKN1CBN',
                'periode': 'Jan 2023 - April 2024',
                'description': 'Membantu pembuatan aset visual untuk konten media sosial dan branding klien.'
            }
        ] 
        
    }

    return render(request, 'main/about.html' , context)

def gallery(request):
    context = {
        'images' : [
            {
                'title' : 'Menjelajah',
                'description' : 'Senang menjelajahi Alam',
                'image' : 'image/foto1.jpg'
            },
            {
                'title' : 'Berkelana',
                'description' : 'Menyusuri Kota',
                'image' : 'image/mySelf.jpeg'
            },
            {
                'title' : 'Olahraga',
                'description' : 'Sepal Bola adalah bagian dari hidup',
                'image' : 'image/bola.jpg',
            }
        ] 
    }

    return render(request, 'main/gallery.html' , context)

