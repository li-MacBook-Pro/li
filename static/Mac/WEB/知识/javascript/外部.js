/*  数据类型：
        1、number数字（数字/小数/NaN）
        2、字符串："" ''
        3、boolean：true或者false
        4、null：对象为空
        5、undefined：未定义，一个变量没有给初始值，则会默认赋值为undefined。
    定义变量：var b=1;var=c;c=2;c="coco";
    console.log(typeof b);
    alert()
    一元运算符：++  -- +（正号）-（负号）
    算术运算符：+ - * / %
    赋值运算符：+ += -= *= /=
    比较运算符：< > =< >= == ===
    逻辑运算符：&& || ! !!
    三元运算符：条件表达式0？表达式1：表达式2
    var b = +'222';//string-->number。
    var flag = +true;//true-->1,false-->0。
    console.log(1>2);//false
    console.log("a">"b");//false
    console.log("b">"a");//true
    console.log("ba">"ab");//true
    console.log("1"==1);//true

    var x=10;console.log(x>20 && x<50);//false
    var x=10;console.log(x>20 || x<50);//true
    var flag=true;console.log(!flag);//取反
    var flag=true;console.log(!!flag);// !! 其他类型转为boolean1、number：0或NaN为false，非0为true
    var str="abc";var str1="";console.log(!!str);console.log(srt1);//string：输了空字符串（""）为false，其他都为true。
    var nu=null;nar=nu2;console.log(!!nu);console.log(!!nar);//null或者undefined都为false
    var date= new Date();console.log(!!date);//对象都是true
    while(true){}

    创建自定义对象
    var obj=new object();
    console.log(obj)
    obj.name="小白"
    obj.sex="男"
    obj.age-12;
    读取对象属性语法：对象名.属性名
    console.log(obj.age);
    console.log(obj.coco);//如果读取对象中没有属性，不会报错，会返回undefined
    修改属性值：对象名.属性值=新值-->有改无增
    obj.name="白安"
    删除对象中属性：delete 对象名.属性值
    delete obj.name;
    数字语法：对象名["12"]=属性值//双引号可有可无吗，读取也需要中括号。
    obj[11]=12;
    console.log(obj[11]);
    属性值：可以是任意数据类型，基本数据类型，对象
    //无限嵌套var obj0={}
    // var obj1={}
    // var obj2={}
    // obj0.test=obj1;
    // obj1.test=obj2;
    // obj2.text=obj0;
    // console.log(obj0)


    函数会覆盖 不传参数undefined
    1、var fun = new Function(形式参数列表，函数体)
    var fun new FUnction("a","b","alert(a)");
    函数名（实际参数）
    fun(100,200)
    2、Function 函数名(形参){alert(a+b);}
        this:在全局执行环境中（在任何函数体外部）this 都指向全局对象。this的值取决于函数被调用的方式。
        function fun(){alter(this);}
        var obj={name:'xx',sayName:fun;}
        obj.sayName();
    Function Car(a,b) {alert(a+b);}
    Car(100,200)

    function Person(name, age, sex) {this.name = name;this.age = age;this.sex = sex;}
    3、构造函数：var 函数名 = Function(形参列表){函数体}：构造函数和普通函数区别，构造函数需要new关键字调用。普通调用返回return值，
        流程1、调用后立即创建一个对象；2、讲创建对象设置为函数this，在构造函数中用this引用新创建对象；3、一行行执行代码；4、讲新创建的对象作为返回值返回。
    function Car(make, model, year) {this.make = make;this.model = model;this.year = year;this.sayName:function(){alert(this.name);}}
    console.log(car1.sayName==car2.sayName);//false
    构造地址不一样，每次创建对象都需要单独创建一个新的，耗费内存，在外面单独一个函数,但是会污染命名空间
    function(){alert(this.name);
    function Car(make, model, year) {this.make = make;this.model = model;this.year = year;this.sayName:function;}}
    console.log(car1.sayName==car2.sayName);//true

    var car1 = new Car("Eagle", "Talon TSi", 1993);
    var car2 = new Car("Nissan", "300ZX", 1992);
    car1.sayName();
    car2.sayName();
    console.log(car1);console.logcarp2);

    



    1、console.log(fun.length)
    2、函数会进行覆盖
    3、不传参数undefined
    4、arguments：对象是所有（非箭头）函数中都可用的局部变量。索引
        function add() {
        console.log(arguments[0]);
        var sum =0,
        for(var i=0; i<arguments.length; i++){sum += arguments[i];}
        return sum;}
        var s= add(11,2,3,4,3,3,23,12)//调用普通函数，返回一个return值
        console.log(s)



 */
// var c=1/0;
// alert(typeof c);
// alert(c);
// console.log('ab'== NaN);//网页控制台输出
// console.log(NaN == NaN);//网页控制台输出
// console.log();
var b = +'222';//string-->number。
var flag1 = +true;//true-->1,false-->0。
console.log(1>2);//false
console.log("a">"b");//false
console.log("b">"a");//true
console.log("ba">"ab");//true
// console.log("1"==1);//true

var x=10;
console.log(x>20 && x<50);//false
console.log(x>20 || x<50);//true
var flag=true;
console.log(!flag);//取反
console.log(!!flag);// !! 其他类型转为boolean1、number：0或NaN为false，非0为true
var str="abc";
var str1="";
console.log(!!str);//!! true
console.log(!!str1);//!!string：输了空字符串（""）为false，其他都为true。
var nu=null;
var nu2;
console.log(!!nu);
console.log(!!nu2);//!!null或者undefined都为false
var date= new Date();
console.log(!!date);//!!对象都是true

if(a<6){}else if(a<6){}else if(a<6){}

var sw=11;//匹配按照全等于来比较
switch(sw)//没有break，从满足条件之后的都会执行完毕。
{case 11:console.log("11");break;
case 12:console.log("12");break;default:console.log("默认最后执行")
}

while(a<10){a++;console.log(a)}
//循环要做的事情，先执行do再运行循环。
do{a++;}while(a<10);

for(var i=0;i<10;i++){console.log(i)}



// var txtDom=document.getElementById("txt");
// txtDom.innerHTML='<h1>我还是我</h1>';
var old=99;
if(old<=44){console.log("青年人")}
if(a<6){}else if(a<6){}else if(a<6){}