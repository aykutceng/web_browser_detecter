ENGLISH:

	1.) You have to install necessary python packages which are in browser_detecter.py. Import packages,

		- pyautogui
		- os
		- tk / tkinter
		- webbrowser

	2.) Put a website address in url variable.(Such as " url = 'website.com' " )

	3.) Write known browser file path in a list. (Which is in path_list variable)

	4) 1- Control if the file exists and open url in first avaible browser. Then break the code!
	    2- If none of them avaible or paths are not correct then let user to choose browser path manually.(using askopenfilename() which part of tkinter)

TÜRKÇE:
	
	1.) browser_detecter.py dosyasında yer alan gerekli python paketleri yüklenmeli ve belirtilmelidir.
		
		- pyautogui
		- os
  		- tk / tkinter
		- webbrowser

	2.) url değişkeninin içerisine bir internet sitesi adresi yazınız.
	
	3.) Bir liste içerisinde tarayıcı dosyalarına ait yolları belirtiniz.(path_list değişkeni içerisindedir)

	4.) 1- Dosya yollarının var olduğunu kontrol edin ve varsa url'yi uygun ilk tarayıcıda açın. Çalışmayı break satırı ile durdurun.
	     2- Eğer belirtilen tarayıcılar yoksa ya da yollar eşleşmiyorsa kullanıcıya manuel olarak tarayıcı yolu seçme izni verin.(Bunun için tkinter içerisinde yer alan askopenfilename() yapısı kullanılarak) 