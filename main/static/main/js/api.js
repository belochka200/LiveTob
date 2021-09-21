new Vue({
    el: '#test',
    data: {
        sights: [] 
    },
    created: function () {
        const vm = this;
        axios.get("/api/sights/")
        .then(function (response) {
            console.log(response.data)
            vm.sights = response.data
        })
    }
})