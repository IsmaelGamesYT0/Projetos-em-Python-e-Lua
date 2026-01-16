local UserInputService = game:GetService("UserInputService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

local defaultWalkSpeed = humanoid.WalkSpeed -- Velocidade padrão (16 studs/s)
local sprintWalkSpeed = 32 -- Velocidade de corrida (ajuste conforme necessário)
local isSprinting = false

-- Função para lidar com a entrada do usuário
UserInputService.InputBegan:Connect(function(input, gameProcessedEvent)
	-- Verifique se a tecla Shift esquerda foi pressionada e se o evento não foi processado por um elemento de interface (UI)
	if input.KeyCode == Enum.KeyCode.W and not gameProcessedEvent then
		isSprinting = true
		humanoid.WalkSpeed = sprintWalkSpeed
	end
end)

-- Função para lidar com o término da entrada do usuário
UserInputService.InputEnded:Connect(function(input)
	-- Verifique se a tecla Shift esquerda foi solta
	if input.KeyCode == Enum.KeyCode.W then
		isSprinting = false
		humanoid.WalkSpeed = defaultWalkSpeed
	end
end)

-- Opcional: Garante que a velocidade padrão seja restaurada se o personagem for redefinido
player.CharacterAdded:Connect(function(newCharacter)
	character = newCharacter
	humanoid = character:WaitForChild("Humanoid")
	defaultWalkSpeed = humanoid.WalkSpeed
	if not isSprinting then
		humanoid.WalkSpeed = defaultWalkSpeed
	end
end)
