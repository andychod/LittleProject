new Vue({
    el : "#app",
    data: {a:1,b:333},
    methods:{
        alert: function()
        {
            alert(this.b);
        }
    }
})