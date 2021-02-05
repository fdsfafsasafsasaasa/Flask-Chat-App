var socket = io();

function sendmessage(){
    date = new Date()
    if(document.getElementById("messagebox").value == null){
        return
    }
    var messagebody = {
        "body": document.getElementById("messagebox").value,
        "user" :  "pakt",
        "date": date
    }
    socket.emit("message_send", messagebody)
};
socket.on("message_recv", data => {
    var message = document.createElement("div");
    message.innerHTML = `<div class="message">${data["user"]}: ${data["body"]}<span></span></div>`
    document.getElementById("messages").appendChild(message)
    $(document).scrollTop($(document).height()); 
    $("#messagecontainer2")[0].reset();
});

$("#messagecontainer2").submit(function(e) {
    e.preventDefault();
});