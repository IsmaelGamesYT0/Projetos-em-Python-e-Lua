local Players = game:GetService("Players")
local player = Players.LocalPlayer

player.CharacterAdded:Connect(function(character)
	local humanoid = character:WaitForChild("Humanoid")
	local animateScript = character:WaitForChild("Animate")

	-- Pega a única animação
	local JumpAnim = script:WaitForChild("JumpAnim")

	-- Track da animação
	local jumpTrack = humanoid:LoadAnimation(JumpAnim)
	jumpTrack.Looped = false

	-- Desativa animação padrão do roblox
	if animateScript:FindFirstChild("jump") then
		for _,v in ipairs(animateScript.jump:GetChildren()) do
			if v:IsA("Animation") then
				v.AnimationId = "rbxassetid://0"
			end
		end
	end

	-- Detectar quando pula e quando toca o chão
	humanoid.StateChanged:Connect(function(old, new)

		-- Quando começa o pulo
		if new == Enum.HumanoidStateType.Jumping then
			jumpTrack:Play()

			-- Quando caiu no chão
		elseif new == Enum.HumanoidStateType.Landed then
			jumpTrack:Stop()
		end
	end)
end)
