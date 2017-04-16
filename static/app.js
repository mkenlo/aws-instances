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
						$scope.responseStatus="Request Status: 200, Ok";
						$scope.responseAlert = "success";						
					}
					else{
						$scope.responseStatus=result.data.message;						
						$scope.responseAlert = "danger";
					}
				})
				.catch(function(error){
					$scope.responseStatus = error;
					$scope.responseAlert = "danger";
				});
				
		};
		
	});