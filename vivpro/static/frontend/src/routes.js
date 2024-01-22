import { createBrowserRouter } from "react-router-dom";
import { View } from "./Components/View";

const routeList = [
  {
    path: "/",
    element: <View />,
  },
];

export const router = createBrowserRouter(routeList);
