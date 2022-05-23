function init() {
  var canvas = document.getElementById("canvas");
  if (canvas.getContext) {
    var ctx = canvas.getContext("2d");

    var pot = new Image();
    var plant = new Image();
    var mood = new Image();
    var face = new Image();

    var imgArr = [pot, plant, face];


    var pageLoaded = false;
    
    pageLoaded = loadListen(imgArr, ctx);

    //example case for functions
    // if(pageLoaded) {
    //   const myTimeout1 = setTimeout(function() {changeImage(imgArr, 2, "/static/images/face3.png", ctx);}, 500);
    //   const myTimeout2 = setTimeout(function() {removeImage(imgArr, 3, ctx);}, 1000);
    // }

    pot.src = "/static/images/potb.PNG";
    plant.src = "/static/images/leaf3.PNG";
    face.src = "/static/images/face0.PNG";

/*     const gameStateResp = new XMLHttpRequest;
    gameStateResp.open("GET","/api/user-gamestate");
    gameStateResp.send();
    var gameStateData;

    gameStateResp.onreadystatechange=function(){
      if(this.readyState==4 && this.status==200){
        console.log("http resp",gameStateResp.response);
        gameStateData=gameStateResp.response;
        console.log("gsd", gameStateData);
      }
    } */

    $.get("/api/user-gamestate",(data)=>{console.log(data)});

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
    }
  }

  return isLoading;
}

function drawArray(arr, ctx) {
  ctx.clearRect(0, 0, 840, 1270);
  for (i of arr) {
    if((i == 0)){continue;}
    else {ctx.drawImage(i, 0, 0);}
  }
}

function changeImage(arr, i, newsrc, ctx) {
  var img = new Image();
  arr[i] = img;
  img.addEventListener("load", function() {drawArray(arr, ctx);}, false);
  img.src = newsrc;
}

function removeImage(arr, i, ctx) {
  arr[i] = 0;
  drawArray(arr, ctx);
}

function breathingExercise() {
//TODO: Implement game logic and dom changes for breathing exercise
}

  
function moodTrack() {
    console.log("moodtrack");
      document
      .getElementById("mood")
      .addEventListener("submit", function () {
        console.log("submitted");
          console.log($.post("/api/mood", { "mood": document.getElementById("mood-entry").value }));
          //modified from https://stackoverflow.com/questions/18490026/refresh-reload-the-content-in-div-using-jquery-ajax
          $("#game-buttons").load(location.href + " #game-buttons");
        });
}

function breathingExercise() {
  document
    .getElementById("finish-breathing")
    .addEventListener("click", function () {
      console.log($.post("/api/breathing"));
      //change image here
      $("#game-buttons").load(location.href + " #game-buttons");
    });
}

function meditationExercise() {
  document
    .getElementById("finish-meditation")
    .addEventListener("click", function () {
      console.log($.post("/api/meditation"));
      $("#game-buttons").load(location.href + " #game-buttons");
    });
}


function journalExercise() {
  journalPrompt();
    document
  .getElementById("journal-form")
  .addEventListener("submit", function () {
      var entryValue = document.getElementById("journal-entry").value;
      console.log($.post("/api/journal", { "prompt_id": "1", "entry": entryValue, }))
    });
    
    function journalPrompt() {
      //var prompt;
      $.get("/api/get-prompt", function (data) {
        prompt = data;
        document.getElementById("journal-prompt").innerHTML =
          "<h4>" + prompt + "</h4>"; 
      });
    }
  }
