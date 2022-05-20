function init() {
    var canvas = document.getElementById("canvas");
    if (canvas.getContext) {
      var ctx = canvas.getContext("2d");



      var pot = new Image();
      var plant = new Image();
      var mood = new Image();
      var face = new Image();
      
      //0 = pot, 1=plant, 2=face, 3=mood
      var imgArr = [pot, plant, face, mood];

      function loadListen(arr) {
        var loaded = 0;
        let len = arr.length;
        for(var i of arr){
          if (i.type = Image){
            i.addEventListener("load",function(){loaded+=1;console.log(loaded);},false);
          } else {
            console.log("arr element not image");
            //TODO: error handling
          }
          i+=1;
        }

        const loadingTime = setInterval(isLoading, 1);

        function isLoading() {
          if(loaded>=len){
            clearInterval(loadingTime);
            drawArray(arr);
          } else {
            console.log("loading, loaded=", loaded);
          }
        }
      }

      function drawArray(arr) {
        for(i of arr){
          //console.log(i);
          ctx.drawImage(i,0,0);
        }
      }

      loadListen(imgArr);

      /* for (i of imgArr){
        //console.log(i);
        i.addEventListener("load", console.log(i), false);
      } */
/* 
      function draw(img) {
        console.log(i);
        ctx.drawImage(img,0,0);
      } */

/*       imgArr[0].addEventListener("load", function(){ctx.drawImage(imgArr[0],0,0);}, false);
      console.log(imgArr[0]); */

/*       pot.addEventListener(
        "load",
        function () {
          ctx.drawImage(pot, 0, 0);
          //ctx.drawImage(plant, 0, 0);
          //ctx.drawImage(mood, 0, 0);
          plant.onload = function () {
              ctx.drawImage(plant, 0, 0);
              mood.onload = function () {
                  ctx.drawImage(mood, 0, 0);
                  face.onload = function () {
                      ctx.drawImage(face, 0, 0);
                  }
              }
          }
        },
        false
      ); */

      /* imgArr[0] = pot.addEventListener("load", function(){ctx.drawImage(pot,0,0);}, false);
      imgArr[1] = plant.addEventListener("load", function(){ctx.drawImage(plant,0,0);}, false);
 */
      pot.src = "../images/potb.png";
      plant.src = "../images/leaf3.png";
      mood.src = "../images/mood-track.png";
      face.src = "../images/face0.png";
      
  
    } else {
      //fallback content here
    }
}