function init() {
  var canvas = document.getElementById("canvas");
  if (canvas.getContext) {
    var ctx = canvas.getContext("2d");
    //getContext - returns a drawing context on the canvas

    var pot = new Image();
    var plant = new Image();
    var mood = new Image();
    var face = new Image();

      //make face dictionaries
  var dict = new Object();
  dict[0] = "/static/images/face-1.PNG";
  dict[1] = "/static/images/face0.PNG";
  dict[2] = "/static/images/face1.PNG";
  dict[3] = "/static/images/face2.PNG";
  dict[4] = "/static/images/face3.PNG";

   //plant state dictionaries
   var plant_dict = new Object();
   plant_dict[0] = "/static/images/leaf1.PNG";
   plant_dict[1] = "/static/images/leaf105.PNG";
   plant_dict[2] = "/static/images/leaf2.PNG";
   plant_dict[3] = "/static/images/leaf205.PNG";
   plant_dict[4] = "/static/images/leaf3.PNG";
   plant_dict[5] = "/static/images/leaf305.PNG";
   plant_dict[6] = "/static/images/leaf4.PNG";
   plant_dict[7] = "/static/images/leaf405.PNG";
   plant_dict[8] = "/static/images/leaf5.PNG";
   plant_dict[9] = "/static/images/leaf505.PNG";
   plant_dict[10] = "/static/images/leaf6.PNG";
   plant_dict[11] = "/static/images/leaf605.PNG";
   plant_dict[12] = "/static/images/leaf7.PNG";
   plant_dict[13] = "/static/images/leaf705.PNG";
   plant_dict[14] = "/static/images/leaf8.PNG";
   plant_dict[15] = "/static/images/leaf805.PNG";
   plant_dict[16] = "/static/images/leaf9.PNG";
   plant_dict[17] = "/static/images/leaf905.PNG";
   plant_dict[18] = "/static/images/leaf10.PNG";
   plant_dict[19] = "/static/images/leaf1005.PNG";
   plant_dict[20] = "/static/images/leaf11.PNG";
 
 


    //array of activity ids
  var activities= [breathing, meditation, journal]

  var face_changed = activityListen(activities, 0);

    //0 = pot, 1=plant, 2=face, 3=mood
    var imgArr = [pot, plant, face, mood];

    var pageLoaded = false;
    
    pageLoaded = loadListen(imgArr, ctx);

    //example case for functions
    if(pageLoaded) {
       const myTimeout1 = setTimeout(function() {changeImage(imgArr, 2, dict[face_changed], ctx);}, 500);
       const myTimeout2 = setTimeout(function() {removeImage(imgArr, 3, ctx);}, 1000);
     }

    var plant_result = plantResult(plant_changed, plant_dict);

    pot.src = "/static/images/potb.png";
    plant.src = "/static/images/leaf1.png";
    mood.src = "/static/images/mood-track.png";
    face.src = "/static/images/face0.png";
    //face.src = dict[face_changed];
    } else {
        //fallback content here
    }
  
  var plant_changed = plantState();
  
}

function plantResult(value, dict){
    //compare with the dictionary values
    if(dict.some(e => e.dict[key1] == value)){
        console.log('exists');
        return dict[key1]
    }
}

function plantState(){
    let plant_state = plant;
    $.get('/user-gamestate', 
    {plant_state:plant_state} )
}

function activityListen(arr, face_state) {
    var actions_fulfilled = 0;
    //check if the element of the array equals the id of the activity - then apply its event listener, and update face variable
    for (var element of arr) {
        if (element == document.getElementById('breathing')){
          console.log("breathing element", actions_fulfilled);
            element.addEventListener('click', function() {
              actions_fulfilled += 1;
              breathingExercise();
              console.log("breathing event", actions_fulfilled);
          }, false);
        }
        else if (element == document.getElementById('journal')){
          console.log("journal element", actions_fulfilled);
            element.addEventListener('click', function() {
                actions_fulfilled += 1;
                journalEntry();
            }, false);
        }
        else if (element == document.getElementById('meditation')){
          console.log("med element", actions_fulfilled);
            element.addEventListener('click',  function() {
                actions_fulfilled += 1; 
                guidedMeditation()
            });
        }
        else{
            console.log("element is the wrong image");
        }
        console.log("face state", face_state);
    }
    face_state += actions_fulfilled;
    face_state += 1;
    return face_state;
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
return false;
}

function guidedMeditation() {
    //implement game logic for the guided meditation
    void(0);
}

function journalEntry() {
    //implement the logic for words of gratitude
    void(0);
}

