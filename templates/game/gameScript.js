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

    var pageLoaded = false;
    
    pageLoaded = loadListen(imgArr, ctx);

    //example case for functions
    if(pageLoaded) {
      const myTimeout1 = setTimeout(function() {changeImage(imgArr, 2, "../images/face3.png", ctx);}, 500);
      const myTimeout2 = setTimeout(function() {removeImage(imgArr, 3, ctx);}, 1000);
    }

    pot.src = "../images/potb.png";
    plant.src = "../images/leaf3.png";
    mood.src = "../images/mood-track.png";
    face.src = "../images/face0.png";
  } else {
    //fallback content here
  }
}

function loadListen(arr, ctx) {
  var loaded = 0;
  let len = arr.length;
  for (var i of arr) {
    if ((i.type = Image)) {
      i.addEventListener(
        "load",
        function () {
          loaded += 1;
          console.log(loaded);
        },
        false
      );
    } else if ((i == 0)) {
      //image has been removed
      continue;
    } else {
      console.log("arr element not image");
      //TODO: error handling
    }
    i += 1;
  }

  const loadingTime = setInterval(isLoading, 1);

  function isLoading() {
    if (loaded >= len) {
      clearInterval(loadingTime);
      drawArray(arr, ctx);
      return true;
    } else {
      console.log("loading, loaded=", loaded);
    }
  }

  return isLoading;
}

function drawArray(arr, ctx) {
  ctx.clearRect(0, 0, 840, 1270);
  for (i of arr) {
    //console.log(i);
    if((i == 0)){continue;}
    else {ctx.drawImage(i, 0, 0);}
  }
}

function changeImage(arr, i, newsrc, ctx) {
  var img = new Image();
  arr[i] = img;
  img.addEventListener("load", function() {console.log("new img", img); drawArray(arr, ctx); console.log("we tried to draw");}, false);
  img.src = newsrc;
}

function removeImage(arr, i, ctx) {
  arr[i] = 0;
  drawArray(arr, ctx);
}

