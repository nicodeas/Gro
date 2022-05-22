function init() {
  $.get("/api/user-gamestate",(data)=>{console.log(data);});
  var data_call = [];
  $.getJSON("/api/user-gamestate", (data)=>{$.each( data, function() {
    $.each().data_call.push();
  })});
  console.log(data_call);
  var user_data = data_call; //JSON.parse(data_call);
  console.log(user_data);
  //console.log(user_data);
  //document.getElementById("mood-submit").addEventListener("click",function() {return;}, false)
  var canvas = document.getElementById("canvas");
  if (canvas.getContext) {
    var ctx = canvas.getContext("2d");

    var pot = new Image();
    var plant = new Image();
    var mood = new Image();
    var face = new Image();

    let mood_record = user_data.mood_recorded;
    //$.get("/api/user-gamestate",function(data){mood_record = data.mood_recorded;console.log(data.mood_recorded);})
    console.log(mood_record);

    //0 = pot, 1=plant, 2=face, 3=mood
    if(user_data.mood_record){
      var imgArr = [pot, plant, face];
    } else {
      var imgArr = [pot, plant, face, mood];
    }

    var pageLoaded = false;
    
    pageLoaded = loadListen(imgArr, ctx);

    //example case for functions
    // if(pageLoaded) {
    //   const myTimeout1 = setTimeout(function() {changeImage(imgArr, 2, "/static/images/face3.png", ctx);}, 500);
    //   const myTimeout2 = setTimeout(function() {removeImage(imgArr, 3, ctx);}, 1000);
    // }

    pot.src = "/static/images/potb.PNG";
    plant.src = "/static/images/leaf3.PNG";
    mood.src = "/static/images/mood-track.PNG";
    face.src = "/static/images/face0.PNG";

    $.get("/user-gamestate",(data)=>{console.log(data)});

    $.post("/breathing");

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
  //document.getElementById("breathing-modal").style.display="block";
  document.getElementById("finish-breathing").addEventListener("click", function (){console.log($.post("/api/breathing"));})
  //$.get("/api/user-gamestate",(data)=>{console.log(data);});
}

function meditationExercise() {
  document.getElementById("finish-meditation").addEventListener("click", function (){console.log($.post("/api/meditation"));})
}

function journalPrompt() {
  document.getElementById("journal-prompt").innerHTML="<h3>prompt</h3>";
}