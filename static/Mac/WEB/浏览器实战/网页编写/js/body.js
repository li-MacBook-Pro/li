// 获取对象
$(function(){
	var box = $(".left1")//获取轮播图所对应的图片
	// 定义数组保存图片路径
	var arr = [
		"https://res.shiguangkey.com/file/2020/7/6/15939990086282701007705.jpg?x-oss-process=image/format,jpg",
		"https://res.shiguangkey.com/file/2020/7/8/15942051743346189756737.jpg?x-oss-process=image/format,jpg",
		"https://res.shiguangkey.com/file/2020/6/30/15935049307407903460103.jpg?x-oss-process=image/format,jpg",
		"https://res.shiguangkey.com/file/201910/25/20191025143357593690275.png"
	];

	// 切换背景图
	function fun(num){
		box.css("background-image","url("+arr[num]+")");
		// num:当前需要切换的图片到底是第几张
		/*switch(num){//筛选函数css地址
			case 1:
				box.css("background-image","url(https://res.shiguangkey.com/file/2020/7/6/15939990086282701007705.jpg?x-oss-process=image/format,jpg)");
				break;
			case 2:
				box.css("background-image","url(https://res.shiguangkey.com/file/2020/7/8/15942051743346189756737.jpg?x-oss-process=image/format,jpg)");
				break;
			case 3:
				box.css("background-image","url(https://res.shiguangkey.com/file/2020/6/30/15935049307407903460103.jpg?x-oss-process=image/format,jpg)");
				break;
			case 4:
				box.css("background-image","url(https://res.shiguangkey.com/file/201910/25/20191025143357593690275.png)");
				break;
		}*/

	}

	// var time = 1;//保存当前是第几张图片
	var time = 0;//代表图片下标

	//耦合性，低耦合。代码之间紧密联系程序

	// 点击右边符号的轮播
	function right(){
		time ++ ;
		if(time>=arr.length){
			time = 0;
		}
		fun(time);
	}
	// 点击左边符号的轮播
	function left(){
		time--;//time = 0
		if(time<0){
			time=arr.length-1;
		}
		fun(time);
	}
	var timer = setInterval(right,3000);//自动轮播
	// 点击右箭头,触发函数
	$(".left1 .ul1 .li2").click(function(){
		clearInterval(timer);//清除定时器标识
		right();
	});
	// 点击左箭头,触发函数
	$(".left1 .ul1 .li1").click(function(){
		clearInterval(timer);//清除定时器标识
		left();
	});
	// 获取圆圈对象

	var lis = $(".left1 .ul2 li");//这是复数
	//console.log(lis[0]);//标签，dom对象
	//转为js对象，添加点击对象。
	/*$(lis[0]).click(function(){
		fun(1);
	});
	$(lis[1]).click(function(){
		fun(2);
	});
	$(lis[2]).click(function(){
		fun(3);
	});
	$(lis[3]).click(function(){
		fun(4);
	});*/

	//数组遍历
	lis.each(function(i){//遍历
		// 给每一个遍历出来的li绑定事件，this是dom对象，转为js对象
		$(this).click(function(){
			fun(i);
			// 给当前点击的元素添加（addClass）class样式,并且其他的兄弟（siblings）元素移除（removeClass）掉class样式
			$(this).addClass("color").siblings().removeClass("color");
				// fun(i+1);
				fun(i);
		});
	});
	// 1.摸清楚流程
	// 2.当点击左右箭头和圆圈时触发对应的函数,这时候定时器可以被关闭
	// 3.当显示的是第几张图片,那么圆圈就要被选中
	// 考试:网页编写页面

	//给导航li绑定点击事件

	$(".left3 ul li").click(function(){
		$(this).addClass("active").siblings().removeClass("active");/*添加，兄弟元素，删除*/
		// 获取当前被点击元素的下标(范围是在兄弟元素)
		var index = $(this).index();//4
		var lis = $(".left4 ul li");/*获取显示的对象*/
		// 与导航栏对应的li显示
		lis.eq(index).removeClass("hide").addClass("show");/*找到元素，移除隐藏，添加元素*/
		// 其他的兄弟元素隐藏
		lis.eq(index).siblings().removeClass("show").addClass("hide");/*找到元素，子哦那工地元素，隐藏元素，添加元素*/
	});
})