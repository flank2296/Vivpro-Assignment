import { createBrowserRouter } from "react-router-dom";
import { TabularView } from "./Components/View";

const routeList = [
  {
    path: "/",
    element: <TabularView />,
  },
];

export const router = createBrowserRouter(routeList);
