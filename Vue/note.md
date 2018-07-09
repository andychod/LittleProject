# vue 筆記

### 官方文件: https://cn.vuejs.org/

- v-if 屬性<br>
當其為ture時，對應的DOM元素才會存在。<br>
例： &lt;div v-if="loading">訊息載入錯誤&lt;/div&gt; 就會在當veu元件中的loading變數為true時才顯示出這個div <br>
- v-shoe 屬性<br>
跟v-if很像，差在當false時是在DOM隱藏，而不是不存在(display:none)
