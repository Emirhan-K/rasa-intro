# Rasa Temel Chatbot Projesi

Bu proje, Rasa tabanlı bir chatbot oluşturmak için kullanılmaktadır. Chatbot, Türkçe dilini anlamak ve anlamlı cevaplar verebilmek üzere tasarlanmıştır.

## Gerekliliklerin Yüklenmesi

Proje için gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu kullanabilirsiniz:

`pip install -r requirements.txt`


## Actions Sunucusunun Çalıştırılması

Chatbotunuzun özel eylemlerini (actions) çalıştırmak için aşağıdaki komutu kullanmanız gerekmektedir:


`rasa run actions`


Bu komut, `actions.py` dosyasındaki eylem işlevlerini tetikler.

## Chatbot'un Çalıştırılması

Rasa projesi içerisinde önceden eğitilmiş bir model var bu modeli kullanmak isterseniz, chatbotu aşağıdaki komutla başlatabilirsiniz:


`rasa shell`


Chatbot, kullanıcıdan gelen metinlere yanıtlar üretecektir.

## Hava Durumu Sorgulama

Chatbot, hava durumu bilgisini sunmak için hava durumu API'sini kullanabilir. Bu projede, chatbotun hava durumunu sorgulayabilecek şekilde
tasarlandığını unutmayın. Hava durumu API'sine bağlantı için gerekli kodu ve nasıl kullanılacağına dair örnekleri koda dahil etmeniz gerekecektir.

## Sistem Saati Sorgulama

Chatbotun sistem saatini sorgulayabilecek şekilde tasarlandığını unutmayın. Proje içerisinde datetime kütüphanesini kullanarak sistem saatini
sorgulayabilir ve buna uygun cevaplar verebilirsiniz.

## Dil Desteği

Bu proje, Türkçe dilini kullanacak şekilde tasarlanmıştır. Dil modelini ve Türkçe veri kümesini kullanarak chatbotunuzun Türkçe metinleri
anlamasını ve buna uygun cevaplar vermesini sağlamalısınız.

---
