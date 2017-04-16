// app.js
'use strict';

angular.module('awsKeyApiApp',[])
	.controller("awsKeyApiCtrl", function($scope, $http){
		
		$scope.reservationList=[];
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
						$scope.responseStatus="Request Status: 200, Ok";
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
		
	});