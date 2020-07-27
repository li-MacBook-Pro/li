//第一题
var old=99;
if(old<=44){console.log("青年人")}
else if(44<old && old<60){console.log("中年人")}
else if(59<old && old<90){console.log("老年人")}
else if(old>89){console.log("长寿老人")}
//第二题
a=1;b=0;while(a<11){b+=a;a++;}console.log(b);
d=0;for(c=1;c<11;c++){d+=c}console.log(d)
//第三题
var date= new Date();console.log(date);
// week="Monday";
week="Tuesday"
// week="Wednesday"
// week="Thursday"
// week="Friday"
// week="Saturday"
// week="Sunday"
switch(week){
    case "Monday":console.log("Monday plan:学习python");
    case "Tuesday":console.log("Tuesday plan:学习pybort");
    case "Wednesday":console.log("Wednesday plan:Web补充");
    case "Thursday":console.log("Thursday plan:数据分析");
    case "Friday":console.log("Friday plan:机器学习");
    case "Saturday":console.log("Saturday plan:sum up");
    case "Sunday":console.log("Sunday plan:have a rest");
    default:console.log("周计划要执行哦～")
}