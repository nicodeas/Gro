function init() {
  var canvas = document.getElementById("canvas");
  const pot_dict = {
    0: "/static/images/face-1.PNG",
    1: "/static/images/face0.PNG",
    2: "/static/images/face1.PNG",
    3: "/static/images/face2.PNG",
    4: "/static/images/face3.PNG",
  };

    //plant state dictionaries
    const plant_dict = {
      0: "/static/images/leaf1.PNG",
      1: "/static/images/leaf105.PNG",
      2: "/static/images/leaf2.PNG",
      3: "/static/images/leaf205.PNG",
      4: "/static/images/leaf3.PNG",
      5: "/static/images/leaf305.PNG",
      6: "/static/images/leaf4.PNG",
      7: "/static/images/leaf405.PNG",
      8: "/static/images/leaf5.PNG",
      9: "/static/images/leaf505.PNG",
      10: "/static/images/leaf6.PNG",
      11: "/static/images/leaf605.PNG",
      12: "/static/images/leaf7.PNG",
      13: "/static/images/leaf705.PNG",
      14: "/static/images/leaf8.PNG",
      15: "/static/images/leaf805.PNG",
      16: "/static/images/leaf9.PNG",
      17: "/static/images/leaf905.PNG",
      18: "/static/images/leaf10.PNG",
      19: "/static/images/leaf1005.PNG",
      20: "/static/images/leaf11.PNG",
    };
  if (canvas.getContext) {
    var ctx = canvas.getContext("2d");

    var pot = new Image();
    var plant = new Image();
    var face = new Image();

    

    var imgArr = [pot, plant, face];


    var pageLoaded = false;
    
    pageLoaded = loadListen(imgArr, ctx);
    
    function plantState(){
      $.get("/api/user-gamestate", (data) => {
       const plant_state = data["plant_state"]
        plant.src = plant_dict[plant_state]
        });
    }
    var plant_changed = plantState();
    
    function potState(){
        $.get("/api/user-gamestate", (data) => {
        const pot_state = data["pot_state"]
        face.src = pot_dict[pot_state]
        });
    }
    var face_changed = potState();

    pot.src = "/static/images/potb.PNG";
    plant.src = plant_changed;
    face.src = face_changed;

    

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
        document.getElementById("mood").onsubmit = function(){
            location.reload(true);
        }
}

function breathingExercise() {
  document
    .getElementById("finish-breathing")
    .addEventListener("click", function () {
      console.log($.post("/api/breathing"));
      //change image here
      $("#game-buttons").load(location.href + " #game-buttons");
    });
    document.getElementById("finish-breathing").onsubmit = function(){
        location.reload(true);
    }
}

function meditationExercise() {
  document
    .getElementById("finish-meditation")
    .addEventListener("click", function () {
      console.log($.post("/api/meditation"));
      $("#game-buttons").load(location.href + " #game-buttons");
    });
    document.getElementById("finish-meditation").onsubmit = function(){
        location.reload(true);
    }
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
    document.getElementById("journal-form").onsubmit = function(){
        location.reload(true);
    }
  }
