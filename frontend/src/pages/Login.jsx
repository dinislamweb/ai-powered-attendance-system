import { useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { FaEye, FaEyeSlash, FaUserGraduate } from "react-icons/fa";

import Card from "../components/Card";
import Input from "../components/Input";
import Button from "../components/Button";
import { getDashboardPath, login } from "../services/authService";

export default function Login() {
  const navigate = useNavigate();
  const [showPassword, setShowPassword] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [feedback, setFeedback] = useState({ type: "", message: "" });

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    setIsSubmitting(true);
    setFeedback({ type: "", message: "" });

    try {
      const response = await login({
        email: data.email,
        password: data.password,
      });

      setFeedback({
        type: "success",
        message: response?.message || "Login successful.",
      });

      const targetPath = getDashboardPath(response?.user);
      navigate(targetPath, { replace: true });
    } catch (error) {
      setFeedback({
        type: "error",
        message: error.message || "Unable to log in. Please try again.",
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 via-blue-50 to-indigo-100 flex items-center justify-center p-4">

      <Card>

        {/* Logo */}
        <div className="flex justify-center">
          <div className="h-20 w-20 rounded-full bg-gradient-to-r from-blue-600 to-indigo-600 flex items-center justify-center shadow-lg">
            <FaUserGraduate className="text-4xl text-white" />
          </div>
        </div>

        {/* System Name */}
        <h1 className="mt-2 text-center text-2xl font-bold text-gray-800 leading-snug">
          Student Attendance <br />
          Management System
        </h1>

        {/* Login Form */}
        <form
        noValidate
        onSubmit={handleSubmit(onSubmit)}
        className="mt-8"
        >
          <Input
          label="Email Address"
          type="email"
          placeholder="Enter your email"
          register={register}
          name="email"
          rules={{
          required: "Email address is required",
          pattern: {
          value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
          message: "Please enter a valid email address",
          },
          }}
          error={errors.email}
          />

          {/* Password */}
          <div className="mb-5">

            <label className="block mb-2 text-sm font-medium text-gray-700">
              Password
            </label>

            <div className="relative">

              <input
                type={showPassword ? "text" : "password"}
                placeholder="Enter your password"
                {...register("password", {
                required: "Password is required",

                minLength: {
                value: 8,
                message: "Password must be at least 8 characters",
                },

                maxLength: {
                value: 50,
                message: "Password cannot exceed 50 characters",
                },
                })}
                className={`w-full rounded-xl border px-4 py-3 outline-none transition-all duration-300 ${
                  errors.password
                    ? "border-red-500"
                    : "border-gray-300 focus:border-blue-600 focus:ring-4 focus:ring-blue-100"
                }`}
              />

              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-4 top-4 text-gray-500 hover:text-blue-600"
              >
                {showPassword ? <FaEyeSlash /> : <FaEye />}
              </button>

            </div>

            {errors.password && (
              <p className="mt-1 text-sm text-red-500">
                {errors.password.message}
              </p>
            )}

          </div>

          {/* Forgot Password */}
          <div className="mb-6 flex justify-end">

            <button
              type="button"
              className="text-sm text-blue-600 hover:underline"
            >
              Forgot Password?
            </button>

          </div>

          {feedback.message && (
            <p
              className={`mb-4 text-sm ${
                feedback.type === "error" ? "text-red-600" : "text-green-600"
              }`}
            >
              {feedback.message}
            </p>
          )}

          {/* Login Button */}
          <Button text="Login" loading={isSubmitting} />

        </form>

        {/* Footer */}
        <p className="mt-8 text-center text-xs text-gray-400">
          © 2026 Innovative Techworks Ltd.
        </p>

      </Card>

    </div>
  );
}