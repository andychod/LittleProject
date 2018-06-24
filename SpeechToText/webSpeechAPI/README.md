# 程式說明
這裡用到的轉換技巧是透過web Speech API<br>
關鍵function是SpeechRecognition，下方為<br>
官方document：<br>
https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition<br>
<br>
### 使用限制
此程式碼必須放在https之下才可以使用，若是http<br>
則無法獲得麥克風的權限，並且目前只支援使用chrom<br>
和firefox瀏覽器開啟。