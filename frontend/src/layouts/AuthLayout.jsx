import { Navigate, Outlet } from "react-router-dom";
import { getDashboardPath, isAuthenticated, getCurrentUser } from "../services/authService";

export default function AuthLayout() {
  if (isAuthenticated()) {
    return <Navigate to={getDashboardPath(getCurrentUser())} replace />;
  }

  return <Outlet />;
}
