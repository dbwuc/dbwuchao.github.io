

// 页面加载完成之后执行
window.onload=function(){
    const btn=document.getElementById('btn');
const btn1=document.getElementById('btn1');
// 给按钮绑定点击事件
btn.addEventListener(
    'click',()=>{
        alert('点我干什么');
    }
);

btn1.onclick=function(){
    alert("hello");
};
// 读取元素节点属性，采用元素.属性名，特例元素.className


var prev=document.getElementById('prev');
var next=document.getElementById('next');
var info=document.getElementById('info');
var img=document.getElementsByTagName("img")[1];
var imgArr=["./全局属性.jpg","./各元素的显示模式.jpg","./节点的属性.jpg"];
var index=0;
prev.onclick=function(){
    console.log(img.src)
    index--;
    if(index<0){
        index=imgArr.length-1;
    }
    // img.src="./全局属性.jpg";
    img.src=imgArr[index];
    // 设置提示文字
info.innerHTML="一共"+imgArr.length+"图片，当前第"+(index+1)+"张"
}
next.onclick=function(){
    // alert("上一张")
    // 修改src的属性
    console.log(img.src)
    index++;
    if(index>imgArr.length-1){
        index=0;
    }
    // img.src="./各元素的显示模式.jpg";
    img.src=imgArr[index];
    // 设置提示文字
info.innerHTML="一共"+imgArr.length+"图片，当前第"+(index+1)+"张"
}
// 选择器的字符串作为参数，可以根据CSS选择器来查询元素节点对象
document.querySelector(".box1 div")


var areaDiv=document.getElementById("areaDiv");
var showMsg=document.getElementById("showMsg");
var moveBox=document.getElementById("moveBox");



areaDiv.addEventListener('mousemove', function(event) {
    // console.log('Mouse X:', event.clientX);
    // console.log('Mouse Y:', event.clientY);
    showMsg.innerHTML=event.clientX+","+event.clientY;
  });

  //随鼠标移动

//   document.addEventListener('mousemove', function(event) {
//     // console.log('Mouse X:', event.clientX);
//     // console.log('Mouse Y:', event.clientY);
//    var x=event.clientX;
//    var y=event.clientY;
//    moveBox.style.left=x+"px";
//    moveBox.style.top=y+"px";

//   });



    var moveBox = document.getElementById("moveBox");
    var moveBox1 = document.getElementById("moveBox1");
    var box_change = document.getElementById("box_change");
    if(box_change.addEventListener){
      box_change.addEventListener('mousewheel',scrollHandler);
      box_change.addEventListener('DOMMouseScroll',scrollHandler);
    }else{
      box_change.attachEvent('onmousewheel',scrollHandler);
    }

    function scrollHandler(event) {
      event=event||window.event;
      var delata=event.wheelDelta||-event.detail;
      if (delata > 0) {
        console.log("向上滚动");
        box_change.style.width=box_change.clientWidth-10+"px";
      } else {
        console.log("向下滚动");
        moveBox.style.width=box_change.clientWidth+10+"px";
      }
    }

    DragEvent(moveBox)
    DragEvent(moveBox1)
    


    function DragEvent( moveBox){
      var isDragging = false;  // 标识是否正在拖拽
      var offsetX, offsetY;    // 鼠标相对于元素的偏移量
    
      // 1. 按下鼠标开始拖拽
      moveBox.addEventListener('mousedown', function(event) {
        isDragging = true;
    
        // 记录鼠标按下时，相对于 moveBox 的偏移量
        offsetX = event.clientX - moveBox.offsetLeft;
        offsetY = event.clientY - moveBox.offsetTop;
    
        // 阻止选中文本等默认操作
        event.preventDefault();
      });
    
      // 2. 鼠标移动时更新位置
      document.addEventListener('mousemove', function(event) {
        if (isDragging) {
          // 计算新的位置
          var x = event.clientX - offsetX;
          var y = event.clientY - offsetY;
    
          // 更新 moveBox 的位置
          moveBox.style.left = x + "px";
          moveBox.style.top = y + "px";
        }
      });
    
      // 3. 鼠标松开时停止拖拽
      document.addEventListener('mouseup', function() {
        isDragging = false;
      });
    }


    var count = document.getElementById("count");
var num=1;

setInterval(function(){
  count.innerHTML = num++;
},1000);

var click_move=document.getElementById("click_move");
var btn03=document.getElementById("btn03");
var timer = null;
click_move.addEventListener('click', function() {
  // 避免重复创建定时器
  if (timer) return;
  // var oldValue=btn03.offsetLeft;
  timer=setInterval(function(){
    oldValue=getStyle(btn03,"left")
    var newValus=oldValue+19;
    if(newValus>800){
      newValus=800;
    }
   
    btn03.style.left=newValus+"px";
    if(newValus==800){
      clearInterval(timer);
    }
  },100)

  
  
 
  })


  function getStyle(obj,name){
    if(window.getComputedStyle){
      return parseInt(getComputedStyle(obj,null)[name]);
    }else{
      return parseInt(obj.currentStyle[name]);
    }
  }



// function toggleSubmenu(menuItem, submenuId) {
//     var submenu = document.getElementById(submenuId);
//     if (submenu.style.display === "block") {
//         submenu.style.display = "none";
//         menuItem.classList.remove('collapsed');
//     } else {
//         submenu.style.display = "block";
//         menuItem.classList.add('collapsed');
//     }
// }


  
 
  

}

