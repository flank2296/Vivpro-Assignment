import React, { useState } from "react";
import { rateSong } from "../services";

export const Rating = (props) => {
  const [rating, setRating] = useState(props?.data?.rating || 0);
  const [hover, setHover] = useState(0);

  const onRateHandler = async (rating) => {
    let trackId = props.data.id;
    await rateSong(trackId, rating);
    setRating(rating)
  }

  return (
    <div className="star-rating">
      {[...Array(5)].map((star, index) => {
        index += 1;
        return (
          <button
            type="button"
            key={index}
            className={index <= (hover || rating) ? "rating on" : "rating off"}
            onClick={() => onRateHandler(index)}
            onMouseEnter={() => setHover(index)}
            onMouseLeave={() => setHover(rating)}
          >
            <span className="star">&#9733;</span>
          </button>
        );
      })}
    </div>
  );
};
