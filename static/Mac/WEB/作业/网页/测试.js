prev.onclick=function(){animate(600);}
next.onclick=function(){animate(-600)}

var timer;
function play(){
timer=setInterval(function(){ //设置间歇调用，时间间隔为1500毫秒
next.onclick() //此处是自动向右切换，如果想设置为向左切换，把next换为prev即可
},1500)
}
play(); //实现自动调用


var container=document.getElementById('container'); //获取最外层的容器元素
function stop(){
clearInterval(timer);
}
container.onmouseover=stop; //当鼠标移动到上方时，清除定时器
container.onmouseout=play; //当鼠标从容器元素上方移走时，进行自动轮播

var buttons=document.getElementById('buttons').getElementsByTagName('span');
var index=1;


function buttonsShow(){
for(var i=0;i<buttons.length;i++){
if(buttons[i].className=='on'){ //如果某个span设置了class='on'，那么就将其的class属性设置为空
buttons[i].className='';
}
}
//数组从0开始，故index需要-1
buttons[index-1].className='on'; //设置下一个span的class属性值为'on'，即是高亮显示
}


prev.onclick=function(){
index-=1;
if(index<1){
index=5;
}
buttonsShow();
animate(600);
}
next.onclick=function(){
//由于上面定时器的作用，index会一直递增下去，而元圆点只有5个，因此需要先做出判断
index+=1;
if(index>5){
index=1;
}
buttonsShow();
animate(-600);
}


//点击任意一个小圆点就切换到所对应的图片
for(var i=0;i<buttons.length;i++){

(function(i){ //使用立即执行函数
buttons[i].onclick=function(){
var clickIndex=parseInt(this.getAttribute('index'));
var offset=600*(index-clickIndex);
animate(offset); //存放鼠标点击之后的位置，用于小圆点的正常显示
index=clickIndex;
buttonsShow();
}
})(i)
}