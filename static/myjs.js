$(document).ready(function(){
                
    var socket =io.connect('127.0.0.1:5000');

        socket.on('connect', function(){
            socket.send('User connected')
        });
        
    socket.on('message',function(msg){
        $('#messages').append('<li>'+msg+'</li>');
        console.log("abc");
        
    });
    $('#sendbtn').on('click',function(){
        socket.send($('#mymsg').val());
        $('#mymsg').val("");
    });
    $('#strt').on('click',function(){
        socket.send($('#name').val());
        $('#name').val("");
    });
});