defmodule AutoGuiEx.Python do
  @mapped_functions [
    :position,
    :moveTo,
    :click,
    :moveRel,
    :dragTo,
    :dragRel,
    :isValidKey,
    :printInfo,
    :getInfo,
    :run,
    :countdown,
    :displayMousePosition,
    :failSafeCheck,
    :hotkey,
    :typewrite,
    :hold,
    :press
  ]

  def start_instance(version \\ 'python') do
    path =
      [:code.priv_dir(:auto_gui_ex), "python"]
      |> Path.join()
      |> to_charlist()

    :python.start([
      {:python_path, path},
      {:python, version}
    ])
  end

  def call_instance(pid, module, function, args \\ []) do
    try do
      case :python.call(pid, module, function, List.wrap(args)) do
        result when function in @mapped_functions ->
          apply(__MODULE__, function, [result])

        _ ->
          raise "That function does not exists or not is mapped yet."
      end
    rescue
      result ->
        apply(__MODULE__, function, [result])
    end
  end

  def stop_instance(pid) do
    :python.stop(pid)
  end

  def failSafeCheck(%{} = _result) do
    raise "PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED."
  end

  def getInfo(result) do
    "#{result}"
    |> Jason.decode!()
    |> Map.put("datetime", DateTime.utc_now())
  end

  def position(result) do
    [x, y] = String.replace("#{result}", ["[", "]", ","], "") |> String.split(" ")

    %{x: String.to_integer(x), y: String.to_integer(y)}
  end

  (@mapped_functions -- [:position, :getInfo])
  |> Enum.each(fn function_name ->
    def unquote(function_name)(_result), do: :ok
  end)
end
