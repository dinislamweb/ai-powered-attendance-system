import { Navigate, Outlet, useLocation } from "react-router-dom";
import { getCurrentUser, getDashboardPath, isAuthenticated } from "../services/authService";

export default function ProtectedRoute({ requiredRole = null }) {
  const location = useLocation();
  const authenticated = isAuthenticated();
  const user = getCurrentUser();
  const userRole = user?.role?.toLowerCase() || user?.userType?.toLowerCase() || "";

  if (!authenticated) {
    return <Navigate to="/login" replace state={{ from: location }} />;
  }

  if (requiredRole && userRole !== requiredRole.toLowerCase()) {
    return <Navigate to={getDashboardPath(user)} replace />;
  }

  return <Outlet />;
}
