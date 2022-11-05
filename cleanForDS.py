
shape_keys_dict = {
    'facs_jnt_JawRight':'jawRight',
    'facs_jnt_JawOpen':'jawOpen',
    'facs_jnt_JawLeft':'jawLeft',
    'facs_jnt_JawForward':'jawForward',
    'facs_jnt_EyeWideRight':'eyeWideRight',
    'facs_jnt_EyeWideLeft':'eyeWideLeft',
    'facs_jnt_EyeBlinkRight':'eyeBlinkRight',
    'facs_jnt_EyeBlinkLeft':'eyeBlinkLeft',
    'facs_ctrl_EyeLookUpRight':'eyeLookUpRight',
    'facs_ctrl_EyeLookUpLeft':'eyeLookUpLeft',
    'facs_ctrl_EyeLookOutRight':'eyeLookOutRight',
    'facs_ctrl_EyeLookOutLeft':'eyeLookOutLeft',
    'facs_ctrl_EyeLookInRight':'eyeLookInRight',
    'facs_ctrl_EyeLookInLeft':'eyeLookInLeft',
    'facs_ctrl_EyeLookDownRight':'eyeLookDownRight',
    'facs_ctrl_EyeLookDownLeft':'eyeLookDownLeft',
    'facs_ctrl_CheekPuff':'cheekPuff',
    'facs_ctrl_BrowInnerUp':'browInnerUp',
    'facs_bs_TongueOut':'tongueOut',
    'facs_bs_NoseSneerRight_div2':'noseSneerRight',
    'facs_bs_NoseSneerLeft_div2':'noseSneerLeft',
    'facs_bs_MouthUpperUpRight_div2':'mouthUpperUpRight',
    'facs_bs_MouthUpperUpLeft_div2':'mouthUpperUpLeft',
    'facs_bs_MouthStretchRight_div2':'mouthStretchRight',
    'facs_bs_MouthStretchLeft_div2':'mouthStretchLeft',
    'facs_bs_MouthSmileRight_div2':'mouthSmileRight',
    'facs_bs_MouthSmileLeft_div2':'mouthSmileLeft',
    'facs_bs_MouthShrugUpper_div2':'mouthShrugUpper',
    'facs_bs_MouthShrugLower_div2':'mouthShrugLower',
    'facs_bs_MouthRollUpper_div2':'mouthRollUpper',
    'facs_bs_MouthRollLower_div2':'mouthRollLower',
    'facs_bs_MouthRight_div2':'mouthRight',
    'facs_bs_MouthPucker_div2':'mouthPucker',
    'facs_bs_MouthPressRight_div2':'mouthPressRight',
    'facs_bs_MouthPressLeft_div2':'mouthPressLeft',
    'facs_bs_MouthLowerDownRight_div2':'mouthLowerDownRight',
    'facs_bs_MouthLowerDownLeft_div2':'mouthLowerDownLeft',
    'facs_bs_MouthLeft_div2':'mouthLeft',
    'facs_bs_MouthFunnel_div2':'mouthFunnel',
    'facs_bs_MouthFrownRight_div2':'mouthFrownRight',
    'facs_bs_MouthFrownLeft_div2':'mouthFrownLeft',
    'facs_bs_MouthDimpleRight_div2':'mouthDimpleRight',
    'facs_bs_MouthDimpleLeft_div2':'mouthDimpleLeft',
    'facs_bs_MouthClose_div2':'mouthClose',
    'facs_bs_EyeSquintRight_div2':'eyeSquintRight',
    'facs_bs_EyeSquintLeft_div2':'eyeSquintLeft',
    'facs_bs_CheekSquintRight_div2':'cheekSquintRight',
    'facs_bs_CheekSquintLeft_div2':'cheekSquintLeft',
    'facs_bs_BrowOuterUpRight_div2':'browOuterUpRight',
    'facs_bs_BrowOuterUpLeft_div2':'browOuterUpLeft',
    'facs_bs_BrowDownRight_div2':'browDownRight',
    'facs_bs_BrowDownLeft_div2':'browDownLeft',
}

def kill_shape_key_driver():
    oj=bpy.context.object
    shape_keys = oj.data.shape_keys
    blocks = shape_keys.key_blocks
    drivers = shape_keys.animation_data.drivers
    for block in blocks:
        shape_key_name=block.name
        try:
            newName=shape_keys_dict[shape_key_name]
        except:
            print("Ignoring shape key", shape_key_name)
        else:
            
            dr = drivers.find(f'key_blocks["{shape_key_name}"].value')
            if dr is not None:
                drivers.remove(dr)
            block.name=newName
        