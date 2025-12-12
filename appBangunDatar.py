import streamlit as st
import math

#halaman utama
st.title ('aplikasi perhitungan luas bangun datar')
st.header('buatan anak sistem informasi')

menu = st.sidebar.selectbox('Menu', ['luas persegi','luas segitiga','luas lingkaran'])
if menu == 'luas persegi':
    st.write('halaman untuk menghitung luas persegi')
    st.image('data:image/webp;base64,UklGRk4DAABXRUJQVlA4IEIDAAAwIACdASr3AOoAPp1OpUylpCQiIlLZKLATiWlu4XBl7mNwst4o/rs25/jM4zjO+ID6W843gZx3ed9/x+VP6p/6vuDiFIKe2XnbnHc47nHc47nHcZZF+7wGSwzOMzI6SL+lE5kPAOTuXSHySjV4HQ8Y3fBD4fzTbdcMys1AHj8k/0AinSjcAs0klEhTpRuAWaSSh6CUVIKZedrFbdK+T/P9HUO70bjZkRAkS+gpuWaSSiQp0o3ALNJJRIU6UavSvSDNXvbeFwOuQ1JkhFsm/1gA6lP8tImRdagy83TjBclBcFmsjOyfaWbS9BrhrYaCybn5NsPbLztzjucdzjucdzjucdzjucdzjubQAAD+/jogitn3BNt69ZdZk1kvx0GXvGxgG/v4ZaAAyUjdSMn84tNIP90q9b/gKdXOJIEg47ouiEFH0XzFP0XDdJKPbZVHkv4fbXSrbB6PdvmNbLWPEC2G2RGvTKaaRTZufmZT//EbOnQbuOBhrD96Xj48z8udQuf0idj9/5jG++jYaOLQnf2YlH1K5EQEc/zpQUoTdRNzeeh/lJR2dKyP/38W/fcmTSLVNBPk588bEdiDa1Rk5exGe9EJvtW2W5eTHAJ5AQp4nrDWNl/c+A0+4hWT3blka6Nx9HrWui1rRO5bQnyeuVzEOkSBz+JfYSSYu/TCPKY3O0CCmhDft8azEf90NvYH2Eb9f/FAvM49bZ2MbVDCGedqoPkfMbBTYkDxakbj+5seoG88r5HU1oQ35KIENftvIH1K7BmGt2CY1M19zW3RKaJmjbdb5MOsEd3G6tkvnw0MQH+/jp93i9EjJ5tAnNqfqXe79fT/Vhfk00vDLwEbY0PWyjjpOf2Z4b1P6ZK8wB+pWpBnV61t76PvLe750JfBZ6eglHfwv42QhELqxJrBjAuPEYIh77uPYHp/6SwGaFV9fRL5wuS9u6p7/jR7jaFEYjqXMn8fauknmGO1kYiurlANOnVSmoB4a2MC/PL0RXMDPEb89OnilYQZWtKUmAI0T+NhTB+9aG+cIdau5xIhGFQX3fNQ70yCPSAHj2TT5TMLwDUPwoaNv6M06XQHOUZCr9sm7fmQBJambUxL+vMAAAAAAAA=', caption='gambar persegi')
    sisi = st.number_input('silahkan masukan sisi', min_value=0,)
    if st.button('hitung'):
        luas = sisi * sisi
        st.write(f'luas persegi adalah {luas}')
    
    
elif menu == 'luas segitiga':
    st.write('halaman untuk menghitung luas segitiga')
    st.image('https://asset-a.grid.id/crop/0x0:0x0/700x0/photo/2020/04/27/2008777398.jpg', caption='gambar segitiga')
    alas = st.number_input('silahkan masukan alas', min_value=0)
    tinggi = st.number_input('silahkan masukan tinggi', min_value=0)
    if st.button('hitung'):
        luas = (alas * tinggi) / 2
        st.write(f'luas segitiga adalah {luas}')
        
elif menu == 'luas lingkaran':
    st.write('halaman untuk menghitung luas lingkaran')
    st.image('https://1.bp.blogspot.com/-B-a-CMAY6SQ/X3EroJJd6UI/AAAAAAAAUBM/zdC5ObY7F8o-EOYBV_zenNkaDRJYeuyjACLcBGAsYHQ/s800/jari-jari-lingkaran.jpg', caption='gambar lingkaran')
    r = st.number_input('silahkan masukan jari-jari', min_value=0)
    
    if st.button('hitung'):
        luas = math.pi * r * r
        st.write(f'luas lingkaran adalah {luas:.2f}')