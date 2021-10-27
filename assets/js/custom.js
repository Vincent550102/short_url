$("#urlForm").submit(function () {
    return false;
});

function fetch_from_server() {
    console.log("AAAA");
    $.ajax({
        url: 'http://127.0.0.1:8080/http://st.vincent55.tw/web',// 跳轉到 action 
        data: {
            url: $("#url").val()
        },
        type: 'POST',
        cache: false,
        success: function (data) {
            show_data(data);

        },
        error: function () {
            // view("異常！"); 
            alert("異常！");
        }
    });
}

function show_data(data) {
    // document.getElementById('#urlModalInner').innerHTML = data;
    $("#urlModalInner").html(data);
    console.log(data);
    $("#urlModal").modal('show');
}

function refresh_main_page() {
    location.reload();
}