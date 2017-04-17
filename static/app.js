// app.js
'use strict';

angular.module('awsKeyApiApp',[])
	.controller("awsKeyApiCtrl", function($scope, $http){
		
		$scope.reservationList=[];
		$scope.savedInstances=[];
		$scope.responseStatus= "Request Status Here";
		$scope.responseAlert = "info";

		$scope.getInstances= function(){
			$http.post("/getInstances", 
				{
					"key":$scope.apikey,
				 	"secretkey":$scope.secretkey
				})
				.then(function(result){
					if (result.data.status != "ERROR"){
						$scope.reservationList = result.data.result.Reservations;
						saveInstances(result.data.result.Reservations);
						$scope.responseStatus="Request Status: Success; Please note that instances will be saved";
						$scope.responseAlert = "success";						
					}
					else{
						$scope.responseStatus=result.data.message;						
						$scope.responseAlert = "danger";
					}
				});
				
				
		};

		function saveInstances(reservationList){
			var send_to_save = function(){
				$http.post('/saveInstances', 
					{"datalist":reservationList}
					).then(function(result){
						console.log(result.message);	
					}).catch(function(error){
						console.log(error);
					});


			};
			send_to_save();
		}
		
		var getSavedInstances = function(){
			$http.get('/allInstances')
			.then(function(result){
				$scope.savedInstances=result.data.instancesItems;
			});
		}
		getSavedInstances();
	});