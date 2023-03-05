import React from "react";
import {Carousel} from "react-bootstrap";
import perro from "../assets/robot1.png";

function CarouselContainer() {
  //critical to set initial state to zero
  const [index, setIndex] = useState(0);

  const handleSelect = (selectedIndex, e) => {
    //adjust index to 0 if greater than index of last slide or less than zero
    //slide indexes are zero-based so yourLasSlideIndex would be 1 I guess
    if (selectedIndex >= yourLastSlideIndex+1 || selectedIndex < 0 ){
            this.setIndex(0);
        } else if (selectedIndex !== index) {
            setIndex(selectedIndex);
        }
  };

  return (
    <Carousel activeIndex={index} onSelect={handleSelect}>
      <Carousel.Item>
                <img
                className="d-block w-100"   
                src={perro}
                alt="First slide"
                />
                <Carousel.Caption>
                <h3>First slide label</h3>
                <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
                <img
                className="d-block w-100"
                src={perro}
                alt="Second slide"
                />
                <Carousel.Caption>
                <h3>Second slide label</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </Carousel.Caption>
            </Carousel.Item>
    </Carousel>
  );
}

render(<CarouselContainer />);