var map=new AMap.Map('about-map',{
   resizeEnable: true,
   zoom:15,
   mapStyle:'darkblue',
   center: [113.94254565,22.53578202]
});
//一街信息
(function yjInfo(){
  var yjInfoCenter=[113.94254565,22.53578202];
  map.setCenter(yjInfoCenter);
  var info=[];
  info.push("<h1 style='font-size: 16px;font-weight:normal;'>蔚来物联科技（深圳）有限公司</h1>");
  var yjInfoWindow=new AMap.InfoWindow({
    content: info.join(""),
  });
  yjInfoWindow.open(map,yjInfoCenter);
})();
