import React, { useState, useEffect, useContext } from "react";

import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import "../../styles/home.css";


export const ListOfRestaurants = () => {
	const { store, actions } = useContext(Context);
	
	useEffect(() => {
        console.log(store.restaurant_auth);
		actions.loadSomeData();
	}, []);

	
    return (
		<div className="container">
			<h1 className="m-5">Restaurants</h1>
			<div className="row flex-row flex-nowrap" style={{ overflowX: "auto" }}>
				{store.restaurants && store.restaurants.map((restaurant, index) => (
					<div key={index} className="col-md-4">
						<div className="card" style={{ width: '18rem' }}>
							<img
								src={restaurant.image_url || "fallback_image_url"}
								alt={restaurant.name}
								className="card-img-top"
								style={{ width: '300px', height: '300px' }}
							/>
							<div className="card-body">
								<h5 className="card-title">{restaurant.name}</h5>
								<p className="card-text">
									<strong>Location:</strong> {restaurant.location} <br />
									<strong>Phone Number:</strong> {restaurant.phone_number}
								</p>
                                <Link to="/">
				                    <button className="btn btn-primary">Book your table now</button>
			                    </Link>
                                
							</div>
						</div>
					</div>
				))}
			</div>
			<Link to="/">
				<button className="btn btn-primary my-5">Back home</button>
			</Link>
		</div>
	);
};