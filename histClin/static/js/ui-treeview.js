var UITreeview = function() {
	"use strict";
	//function to initiate jquery.dynatree
	var runTreeView = function() {
		//Default Tree
		$('#tree').jstree({
			"core" : {
				"themes" : {
					"responsive" : true
				}
			},
			"types" : {
				"default" : {
					"icon" : "fa fa-folder text-yellow fa-lg"
				},
				"file" : {
					"icon" : "fa fa-file text-azure fa-lg"
				}
			},
			"plugins" : ["types"]
		});

		//Checkbox
		
		
	};
	return {
		//main function to initiate template pages
		init : function() {
                    runTreeView();
		}
	};
}();
