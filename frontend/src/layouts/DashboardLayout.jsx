import { Link, Navigate, Outlet } from "react-router-dom";
import { getCurrentUser, isAuthenticated, logout } from "../services/authService";

export default function DashboardLayout() {
  const user = getCurrentUser();

  if (!isAuthenticated()) {
    return <Navigate to="/login" replace />;
  }

  const handleLogout = () => {
    logout();
    window.location.href = "/login";
  };

  return (
    <div className="min-h-screen bg-slate-100">
      <nav className="border-b border-slate-200 bg-white px-6 py-4 shadow-sm">
        <div className="mx-auto flex max-w-6xl items-center justify-between">
          <div>
            <h1 className="text-lg font-semibold text-slate-800">Attendance System</h1>
            <p className="text-sm text-slate-500">
              Signed in as {user?.name || user?.email || "User"}
            </p>
          </div>
          <div className="flex items-center gap-4">
            <Link to="/admin-dashboard" className="text-sm text-blue-600 hover:underline">
              Admin
            </Link>
            <Link to="/teacher-dashboard" className="text-sm text-blue-600 hover:underline">
              Teacher
            </Link>
            <Link to="/student-dashboard" className="text-sm text-blue-600 hover:underline">
              Student
            </Link>
            <button
              type="button"
              onClick={handleLogout}
              className="rounded-lg bg-slate-800 px-4 py-2 text-sm text-white hover:bg-slate-700"
            >
              Logout
            </button>
          </div>
        </div>
      </nav>

      <main className="mx-auto max-w-6xl px-6 py-8">
        <Outlet />
      </main>
    </div>
  );
}
