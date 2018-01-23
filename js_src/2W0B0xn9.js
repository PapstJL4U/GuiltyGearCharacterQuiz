emotemultiplier = 1; // Multiplier for how much emotional/subjective qualities affect results - becomes 1.5 if player specifies this is important to him or her
doubleplay = 0; // Value for double playstyle. To be given 0.5 if zoning or rushdown are given a positive value. If it's 1, the doubleplay question is revealed.

function addEmotion(name) {
	$.each(chardata.characters, function(i, v) {
		if (v.charname.indexOf(name) > -1) {
			v.Points=v.Points+(1*emotemultiplier);
			return;
		}
	});
}

function hateEmotion(name) {
	$.each(chardata.characters, function(i, v) {
		if (v.charname.indexOf(name) > -1) {
			v.Points=v.Points-(1*emotemultiplier);
			return;
		}
	});
}

$( document ).ready(function() {
	$.ajaxSetup({ cache: false });
	$('#doubleplay').hide(0);
	$('#results').hide(0);
	$.getJSON( "./profiles.json", function( data ) {
	  var items = "";
	  
	$( ".storyQ img" ).click(function() {
		var charname = $( this ).attr('id');
		var res = charname.split(".");
		var charname = res[0];
		addEmotion(charname);
	});
	$( ".hateQ img" ).click(function() {
		var charname = $( this ).attr('id');
		var res = charname.split(".");
		var charname = res[0];
		hateEmotion(charname);
	});
	
	$( ".question a" ).click(function() {
		$(this).parent().closest('.question').hide(100);
	});
	
	/*  // For debugging purposes
	$( document ).click(function() {
		getResults();
	});
	*/


	  

	
	//  for (i = 0;i < data.characters.length;i++) {
	//	items = items+' '+data.characters[i].charname + ' ' + data.characters[i].Points + ' tier';		
	//  }
	  
	//  alert(items);
	chardata = data;

	 
	});
});

function upgradeTier(tier) {
	$.each(chardata.characters, function(i, v) {
		if (v.Tier == tier) {
			v.Points++;
			return;
		}
	});
}

function pickPlaystyle(playstyle) {
	if (playstyle == "Emotional") {
		emotemultiplier = 1.5;
		return
	}
	$.each(chardata.characters, function(i, v) {
		if (v.Playstyle == playstyle) {
			v.Points++;
			return;
		}
	});
}

function playerSkill(skill) {
	$.each(chardata.characters, function(i, v) {
		if (v.Skill == skill) {
			v.Points++;
			return;
		}
	});
}

function playerGoal(goal) {
	$.each(chardata.characters, function(i, v) {
		if (v.SkillGoal == goal) {
			v.Points++;
			return;
		}
	});
}

function doZoning(factor) {
	if (factor > 0) {
		playPriority();
	}
	$.each(chardata.characters, function(i, v) {
		var modifier = (factor * v.Zoning);
		v.Points=v.Points+modifier;
		return;
	});
}

function doRushdown(factor) {
	if (factor > 0) {
		playPriority();
	}
	$.each(chardata.characters, function(i, v) {
		var modifier = (factor * v.Rushdown);
		v.Points=v.Points+modifier;
		return;
	});
}

function playPriority() {
	doubleplay = doubleplay+0.5;
	if (doubleplay == 1) {
		$('#doubleplay').show(0);
	}
}

function doDoublePlay(factor) {
	$.each(chardata.characters, function(i, v) {
		if (v.Zoning > 0 && v.Zoning < 1 && v.Rushdown > 0 && v.Rushdown < 1) {
			var increase = (v.Zoning*factor)+(v.Rushdown*factor);
			//alert("Increase of "+increase+"!");
			v.Points = v.Points + increase;
			return;
		}
	});
}

function playerFocus(focus) {
	$.each(chardata.characters, function(i, v) {
		if (v.Focus.indexOf(focus) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerRange(range) {
	$.each(chardata.characters, function(i, v) {
		if (v.Range.indexOf(range) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerGender(gender,factor) {
	$.each(chardata.characters, function(i, v) {
		if (v.Gender.indexOf(gender) > -1) {
			v.Points=v.Points+factor;
			return;
		}
	});
}

function playerCharge(charge) {
	$.each(chardata.characters, function(i, v) {
		if (v.Charge.indexOf(charge) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerGimmick(gimmick) {
	$.each(chardata.characters, function(i, v) {
		if (v.Gimmick.indexOf(gimmick) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerMixups(mixup) {
	$.each(chardata.characters, function(i, v) {
		if (v.Mixups.indexOf(mixup) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerMoral(moral) {
	$.each(chardata.characters, function(i, v) {
		if (v.Moral.indexOf(moral) > -1) {
			v.Points = v.Points + emotemultiplier;
			return;
		}
	});
}

function playerOne(oneplayer) {
	$.each(chardata.characters, function(i, v) {
		if (v.OnePlayer.indexOf(oneplayer) > -1) {
			v.Points++;
			return;
		}
	});
}


function playerPriority(priority) {
	$.each(chardata.characters, function(i, v) {
		if (v.Priority.indexOf(priority) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerProjectile(projectile) {
	$.each(chardata.characters, function(i, v) {
		if (v.Projectile.indexOf(projectile) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerReliant(reliance) {
	$.each(chardata.characters, function(i, v) {
		if (v.Reliance.indexOf(reliance) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerResource(resource) {
	$.each(chardata.characters, function(i, v) {
		if (v.Resource.indexOf(resource) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerReversal(reversal) {
	$.each(chardata.characters, function(i, v) {
		if (v.Reversal.indexOf(reversal) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerSetPlay(setplay) {
	$.each(chardata.characters, function(i, v) {
		if (v.SetPlay.indexOf(setplay) > -1) {
			v.Points++;
			return;
		}
	});
}


function playerStances(stance) {
	$.each(chardata.characters, function(i, v) {
		if (v.Stances.indexOf(stance) > -1) {
			v.Points++;
			return;
		}
	});
}

function playerVortex(vortex) {
	$.each(chardata.characters, function(i, v) {
		if (v.Vortex.indexOf(vortex) > -1) {
			v.Points++;
			return;
		}
	});
}

function getResults() {
	var arr = [""];
	var results = [""];
	var results2 = [""];
	var runner = [""];
	var runner2 = [""];
	var inc = 0;
	var cre = 0;
	
	for (i = 0;i < chardata.characters.length;i++) {
		arr[i] = chardata.characters[i].Points;		
		//alert(chardata.characters[i].Points);
	}
	for (i = 0;i< chardata.characters.length;i++) {
		if (chardata.characters[i].Points == Math.max.apply(null, arr)) {
			//alert("Doing with "+chardata.characters[i].fullname);
			results[inc] = chardata.characters[i].fullname;
			//alert("Name should be "+chardata.characters[i].fullname+" and it is "+results[inc]);
			results2[inc] = chardata.characters[i].charname;
			//alert("Secondary name should be "+chardata.characters[i].charname+" and it is "+results2[inc]);
			inc++;
		}
		else if (chardata.characters[i].Points < Math.max.apply(null, arr) && chardata.characters[i].Points >= (Math.max.apply(null, arr)-1)) {
			runner[cre] = chardata.characters[i].fullname;
			runner2[cre] = chardata.characters[i].charname;
			cre++;
		}
	}

	//alert(results[0]);
	//alert(results2[0]);
	//alert(arr);
	//alert(runner);
	title = ("<h2>You got: "+results[0]+"!</h2>");
	img = ("<img src='char/"+results2[0]+".png'>");
	other = "";
	runners = "";
	if (results.length > 1) {
		other = "<p>Other characters you tied for:</p><ul>";
		for (i=1;i<results.length;i++) {
			other = (other+"<li>"+results[i]+"</li>");
		}
		other = other+"</ul>";
	}
	if (runner.length > 0) {
		runners = "<p>Close second characters:</p><ul>";
		for (i=0;i<runner.length;i++) {
			runners = (runners+"<li>"+runner[i]+"</li>");
		}
		runners = runners+"</ul>";
	}

	resultshtml = title+img+other+runners;
	$('#results').html(resultshtml);
	$('#results').show(500);
	$('#results').promise().done(function(){
		$("html, body").animate({ scrollTop: $(document).height() }, 1000);
	});		
	
}