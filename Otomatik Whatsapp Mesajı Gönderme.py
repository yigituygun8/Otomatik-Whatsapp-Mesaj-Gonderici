import pywhatkit  # whatsapp python module

phone_number = str(input("Mesajı Göndereceğiniz Numarayı Alan Koduyla Beraber Giriniz:"))
your_message = str(input("Mesajınız Nedir?:"))
sending_time = int(input("Saat Kaçta Göndermek İstiyorsunuz? (akrep):"))
sending_time2 = int(input("Saat Kaçta Göndermek İstiyorsunuz? (yelkovan):"))

pywhatkit.sendwhatmsg(phone_number, your_message, sending_time, sending_time2, 5)