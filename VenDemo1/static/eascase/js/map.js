var map=new AMap.Map('about-map',{
   resizeEnable: true,
   zoom:15,
   mapStyle:'darkblue',
   center: [111.622033,40.80686]
});
//一街信息
(function yjInfo(){
  var yjInfoCenter=[111.622033,40.80686];
  map.setCenter(yjInfoCenter);
  var info=[];
  info.push("<h1 style='font-size: 16px;font-weight:normal;'>呼和浩特一街科技</h1>");
  // info.push("<p>电话：0471-2526042/400-666-4566</p>");
  // info.push("<p>公司邮箱：admin@eacase.com</p>");
  // info.push("<p>地址：内蒙古呼和浩特市新华西街回民区政府斜对面金葫芦科技大厦15楼</p>");
  var yjInfoWindow=new AMap.InfoWindow({
    content: info.join(""),
  });
  yjInfoWindow.open(map,yjInfoCenter);
})();
