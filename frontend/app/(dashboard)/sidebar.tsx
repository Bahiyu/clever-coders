// import { Logo } from "./logo";
import { SidebarRoutes } from "./sidebar-routes";

export const Sidebar = () => {
  return (
    <aside className="hidden lg:flex fixed mt-10 flex-col w-[300px] left-0 shrink-0">
      {/* <Logo /> */}
      <SidebarRoutes />
    </aside>
  );
};
