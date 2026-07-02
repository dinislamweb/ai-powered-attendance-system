export default function Input({
  label,
  type,
  placeholder,
  register,
  name,
  rules = {},
  error,
}) {
  return (
    <div className="mb-5">
      <label className="block mb-2 text-sm font-medium text-gray-700">
        {label}
      </label>

      <input
        type={type}
        placeholder={placeholder}
        {...register(name, rules)}
        className={`
          w-full
          rounded-xl
          border
          px-4
          py-3
          outline-none
          transition-all
          duration-300
          ${
            error
              ? "border-red-500 focus:ring-red-100"
              : "border-gray-300 focus:border-blue-600 focus:ring-4 focus:ring-blue-100"
          }
        `}
      />

      {error && (
        <p className="mt-1 text-sm text-red-500">
          {error.message}
        </p>
      )}
    </div>
  );
}