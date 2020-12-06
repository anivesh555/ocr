

var socket = io.connect(location.protocol+'//' + document.domain + ':'+location.port);
// socket.on('connect', function() {
// 	socket.emit('my event', {data: 'I\'m connected!'});
//     });
 

 // function send(){
 // 	socket.emit('msg' ,'hello')
 // }
function send() {
	var msgBox = document.getElementById('msgBox')
	socket.emit('msg' ,msgBox.value)
	msgBox.value='' 
}  
// 2nd creat var of msgzBox 



socket.on('push',function(data){
	
	// console.log(data)
	var msgList= document.getElementById('msgList')
	msgList.innerHTMl+="<p>"+data+'<p>'
})
// 	a=(l*b)
// 	return a
// }

// a1 =area(4,5)





// for (var i=1 ,i<=5 ,i++) {
// 	console.log(i)
// }\



function fetchusers(){
	fetch('/getusers').then(function(res){
		res.json().then(function(data){
			console.log(data)
		})
	}) 
}